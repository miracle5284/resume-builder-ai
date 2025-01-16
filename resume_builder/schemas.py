from pydantic import BaseModel
from fastapi import UploadFile, Form, File

class Query(BaseModel):
    """
    Represents the input query data for the resume builder.
    """

    job_posting_url: str
    github_url: str
    personal_writeup: str
    resume_file: UploadFile

    @classmethod
    def as_form(
            cls,
            job_posting_url: str = Form(...),
            github_url: str = Form(...),
            personal_writeup: str = Form(...),
            resume_file: UploadFile = File(...),
    ):
        """
        Converts form data into a Query object.

        Returns:
            Query: A Pydantic model instance populated with form data.
        """
        return cls(
            job_posting_url=job_posting_url,
            github_url=github_url,
            personal_writeup=personal_writeup,
            resume_file=resume_file
        )

    def pop(self, field):
        """
        Removes a field from the model and returns its value.

        Args:
            field (str): The name of the field to remove.

        Returns:
            Any: The value of the removed field.

        Raises:
            AttributeError: If the field does not exist.
        """
        if hasattr(self, field):
            value = getattr(self, field)
            delattr(self, field)
            return value
        raise AttributeError(f"Field `{field}` doesn't exist")