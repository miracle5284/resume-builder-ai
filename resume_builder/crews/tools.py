from crewai_tools import (
    FileReadTool,
    ScrapeWebsiteTool,
    MDXSearchTool,
    SerperDevTool,
    PDFSearchTool
)

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

def get_reader_tool(file_path):
    reader_tool = FileReadTool(path=file_path)
    return reader_tool

def get_semantic_search_tool(file_path):
    semantic_search_tool = PDFSearchTool(pdf=file_path)
    return semantic_search_tool

