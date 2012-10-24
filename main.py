import webapp2

from gae_mini_profiler import profiler

application = webapp2.WSGIApplication([
    ("/gae_mini_profiler/request", profiler.RequestStatsHandler),
    ("/gae_mini_profiler/shared", profiler.SharedStatsHandler),
])
