class Config(object):
    """Common Configuration."""

    def __init__(self, arg):
        super(Config, self).__init__()
        self.arg = arg


class DevelopmentConfig(Config):
    """Put all Development level Configuration."""

    DEBUG = True

    def __init__(self, arg):
        super(DevelopmentConfig, self).__init__(arg)


class ProductionConfig(Config):
    """Put all Production level Configuration."""
    DEBUG = False

    def __init__(self, arg):
        super(ProductionConfig, self).__init__(arg)


app_config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
