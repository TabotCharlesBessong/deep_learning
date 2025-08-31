
from src.cnnClassifier import logger
# from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Starting the application...")

STAGE_NAME = "Data Ingestion stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e