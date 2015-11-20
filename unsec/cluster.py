from unsec import EmailCollection

class Cluster(EmailCollection):
    def __init__(self):
        super(Cluster,self).__init__()
        self.centroids = None

    def get_dispersion(self):
        pass




