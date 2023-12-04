
with open("/workspaces/aoc-2023/2/input.txt", "r") as input:
    possible_game_ids = []
    cube_powers_list = []
    rgb = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    lines = [line.rstrip('\n') for line in input.readlines()]
    for game in lines:
        game_id = int(game.split(":")[0].split(" ")[1])
        sets = game.split(":")[1].split(";")
        max_in_set = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for color_set in sets:
            values = color_set.split(",")
            for color in values:
                count = int(color.strip().split(" ")[0])
                color_str = color.strip().split(" ")[1]
                max_current = max(max_in_set[color_str], count)
                max_in_set[color_str] = max_current

        if rgb["red"] >= max_in_set["red"] and rgb["blue"] >= max_in_set["blue"] and rgb["green"] >= max_in_set["green"]:
            possible_game_ids.append(game_id)

        cube_powers_list.append(max_in_set["blue"] * max_in_set["green"] * max_in_set["red"])

    print(sum(possible_game_ids))
    print(sum(cube_powers_list))
    