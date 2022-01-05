if __name__ == "__main__":

    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }

    for item in languages.items():
        print("{} was created by {}".format(item[0], item[1]))
