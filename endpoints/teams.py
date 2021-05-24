import json

from engine.e2e.platforms.teams.parser import Parser
from engine.e2e.builder import OutputBuilder

def profile_builder(convoId, userId):
    pass


def handler(event, context):
    event_body = json.loads(event['body'])
    print(event_body)

    parser = Parser(event_body)

    userObject = {
        "id": parser.id,
        "convoId": parser.convoId,
        "serviceUrl": parser.serviceUrl
    }

    outputBuilder = OutputBuilder(parser)
    outputBuilder.typing_action()


