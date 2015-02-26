from pipeline import pipeline


def launch_clustering(request, token):
   return pipeline(token)
