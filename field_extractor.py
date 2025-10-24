"""
Field extraction using OpenAI GPT
"""

import openai
import json
import re

class FieldExtractor:
    def __init__(self, api_key):
        openai.api_key = api_key
