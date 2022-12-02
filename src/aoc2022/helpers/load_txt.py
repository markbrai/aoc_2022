from pathlib import Path

import numpy as np


def load_txt_to_list(
    day: int, line_type: str, start: int = None, end: int = None, name: str = "input"
) -> list:

    day_str = "day" + str(day)

    path_parts = f"{day_str}_{name}.txt"
    file_path = Path.cwd() / "input" / path_parts

    with open(file_path, "r") as input_file:

        lines = input_file.readlines()[start:end]

        if line_type == "int":
            input_list = [int(i) for i in lines]
        elif line_type == "str":
            input_list = lines
        elif line_type == "matrix":
            input_list = get_matrix_from_txt(lines)

    return input_list


def get_matrix_from_txt(lines: list) -> list:

    matrices = []
    matrix = []

    lines = [line.strip().split(" ") for line in lines]

    for line in lines:
        if line[0] != "":
            row = [int(i) for i in line if i != ""]
            matrix.append(row)
            # print(row)

        else:
            # print("gap!")
            matrices.append(matrix)
            matrix = []

    # Append the last matrix if no blank line after
    matrices.append(matrix)

    nd_matrices = [np.array(matrix) for matrix in matrices]

    return nd_matrices
