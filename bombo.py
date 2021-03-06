from typing import List
import utils

"""
Script para el sorteo de los bombos
"""


def get_data() -> List[str]:
    data = utils.get_data(data_path="data/all_teams.csv")
    return list(map(lambda x: x[0], data))


def generate() -> List[str]:
    """Generate the random indedes for bombo"""
    data = get_data()
    max_teams = len(data)

    index_list = [i for i in range(1, max_teams + 1)]
    # shuffle the list:
    utils.shuffle(index_list)

    bombo = []
    for i in index_list:
        bombo.append(data[i-1])

    return bombo


def print_bombo(bombo):
    for n in range(0, len(bombo)):
        print(n + 1, bombo[n])


if __name__ == "__main__":
    print_bombo(generate())
