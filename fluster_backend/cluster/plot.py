from pipeline import pipeline
import matplotlib.pyplot as plt


def run():
    token = 'gqdzXagRC3oAAAAAAAAATIWc6pemPjW1SzoC58xKeBp0sawdmAsLFREcoCGh-mI_'
    print 'passing off to pipeline...'
    X, labels = pipeline(token)
    print 'returned X, labels'
    colors = ['#FF6600', '#CC0000', '#33CCFF', '#006633']
    for point, label in zip(X, labels):
        x = point[0]
        y = point[1]
        plt.scatter(x, y, color=colors[label])
    plt.show()

if __name__ == '__main__':
    run()
