import requests
import coderclient.prompt
import coderclient.models
import jinja2
import logging

class CoderClient():
    def __init__(self, url: str, codebook: coderclient.models.Codebook):
        self._url = url.strip("/") + "/%s"

        template_env = jinja2.Environment(loader = jinja2.PackageLoader("coderclient"))
        self._prompt_template = template_env.get_template("prompt.j2")
        self._codebook = codebook

    def code(self, document: str):
        prompt = self._prompt_template.render(document = document, codebook = self._codebook)
        schema = self._codebook.jsonschema
        logging.debug("Prompt: "+ prompt)
        logging.debug("Schema: "+ str(schema))
        return requests.post(
                self._url % "completion", 
                json = {
                    "prompt": prompt,
                    "n_predict": 128,
                    "json_schema": schema
                    }
                ).json()["content"]
