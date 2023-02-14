from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.metrics import MetricUnit

logger = Logger(service="APP")
tracer = Tracer(service="APP")
metrics = Metrics(namespace="MyApp", service="APP")
connect_app = ApiGatewayResolver()

@connect_app.get("/connect/<source>/<dest>")
@tracer.capture_method
def connect(source, dest):
    tracer.put_annotation(key="source", value=source)
    tracer.put_annotation(key="dest", value=dest)
    return {"source": source, "dest": dest, "connected": True}

@tracer.capture_lambda_handler
@logger.inject_lambda_context(
    correlation_id_path=correlation_paths.API_GATEWAY_REST, log_event=True
)
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event, context):
    try:
        return connect_app.resolve(event, context)
    except Exception as e:
        logger.exception(e)
        raise
