from google.appengine.api import lib_config
from appengine_config import appstats_should_record

# If using the default should_profile implementation, the profiler
# will only be enabled for requests made by the following GAE users.
enabled_profiler_emails = [
                           ]


# Customize should_profile to return true whenever a request should be profiled.
# This function will be run once per request, so make sure its contents are fast.
class ProfilerConfigProduction:
    @staticmethod
    def should_profile(environ):
        return appstats_should_record(environ)

class ProfilerConfigDevelopment:
    @staticmethod
    def should_profile(environ):
        return appstats_should_record(environ)

# see http://code.google.com/appengine/docs/python/tools/appengineconfig.html
_config = lib_config.register('gae_mini_profiler',
                              {'ENABLED_PROFILER_EMAILS': enabled_profiler_emails,
                               'ConfigProduction': ProfilerConfigProduction,
                               'ConfigDevelopment': ProfilerConfigDevelopment})
