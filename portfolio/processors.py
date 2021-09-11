from pathlib import Path

from portfolio.app.core import App
from portfolio.configs import Configs

# main server processors
configs = Configs(package_dir=Path(__file__).parent)
app = App(configs=configs)
