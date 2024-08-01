
from loguru import logger

print("essa mensagem")

logger.debug("Um aviso para o desenvolvedor (ou eu mesmo) no futuro")
logger.info("Informacao importante do processo")
logger.warning("Um aviso que algo vai parar de funcionar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu uma que aborta a aplicacao")