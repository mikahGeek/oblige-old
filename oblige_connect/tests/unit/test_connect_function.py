import json

from src.connect import connect


def test_lambda_handler_connect(apigw_connect_event, lambda_context):
    ret = connect.lambda_handler(apigw_connect_event, lambda_context)
    expected = json.dumps({"source": "a", "dest": "b", "connected": True}, separators=(",", ":"))

    assert ret["statusCode"] == 200
    assert ret["body"] == expected

