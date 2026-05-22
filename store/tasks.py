from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def log_product_created(product_name):
    logger.info("Создан новый товар: %s", product_name)
    return product_name