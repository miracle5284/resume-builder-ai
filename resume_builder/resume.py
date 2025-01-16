import re
from crewai import Agent, Task, Crew
from .param_config import agents as agent_configs, tasks as task_configs


class ResumeCrew:
    """
    Manages a crew of agents and tasks for resume processing.

    This class is responsible for initializing agents and tasks, interpolating variables,
    and building a cohesive crew that can execute assigned tasks.
    """

    def __init__(self, agents, tasks):
        """
        Initializes the ResumeCrew with agents and tasks.

        Args:
            agents (dict): A dictionary where keys are agent names and values are their configurations.
            tasks (dict): A dictionary where keys are task names and values are their configurations.
        """
        self.agents = []  # List to store initialized agent names
        self.tasks = []  # List to store initialized task names
        self._crew = None  # Placeholder for the Crew instance

        # Initialize agents
        for agent, params in agents.items():
            self.agents.append(agent)
            setattr(self, agent, Agent(**{**agent_configs[agent], **params}))

        # Initialize tasks
        for task, params in tasks.items():
            setattr(self, task, Task(**{**task_configs[task], **self.interpolate(params)}))
            self.tasks.append(task)

    def retrieve_variable(self, variable):
        """
        Retrieves the value of a variable, interpolating if necessary.

        Args:
            variable (str): The variable to retrieve, which may contain placeholders in the format {{variable_name}}.

        Returns:
            The interpolated value if the variable contains a placeholder; otherwise, the variable itself.
        """
        pattern = re.compile(r"\{\{(\w+)\}\}")  # Regex to match placeholders
        match = re.search(pattern, variable)
        return match and getattr(self, match.group(1)) or variable

    def interpolate(self, obj):
        """
        Recursively interpolates variables within an object.

        Args:
            obj: The object to interpolate. Can be a string, dictionary, list, or tuple.

        Returns:
            The interpolated object with all placeholders replaced by their values.
        """
        if isinstance(obj, str):
            return self.retrieve_variable(obj)
        elif isinstance(obj, dict):
            return {k: self.interpolate(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [self.interpolate(items) for items in obj]
        return obj

    def build_crew(self):
        """
        Builds the Crew instance by combining all initialized agents and tasks.

        Returns:
            Crew: An instance of the Crew class ready for execution.
        """
        crew = Crew(
            agents=[getattr(self, agent) for agent in self.agents],
            tasks=[getattr(self, task) for task in self.tasks],
            verbose=True
        )
        return crew

    @property
    def crew(self):
        """
        Lazy property to retrieve or build the Crew instance.

        Returns:
            Crew: The initialized Crew instance.
        """
        if self._crew is None:
            self._crew = self.build_crew()
        return self._crew
