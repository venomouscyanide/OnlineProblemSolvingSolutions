# https://leetcode.com/problems/maximum-units-on-a-truck/

def run(box_types, truck_size):
    # num_boxes, box_weight
    sorted_boxes = sorted(box_types, key=lambda x: x[1], reverse=True)
    current_tally = 0
    current_prd = 0
    for num_boxes, box_weight in sorted_boxes:
        potential = current_tally + num_boxes
        if potential <= truck_size:
            current_tally += num_boxes
            current_prd += num_boxes * box_weight
        else:
            difference = truck_size - current_tally
            if num_boxes < difference:
                continue
            current_tally += difference
            current_prd += difference * box_weight

    return current_prd


if __name__ == '__main__':
    box_types = [[1, 3], [2, 2], [3, 1]]
    truck_size = 4
    print(run(box_types, truck_size))

    box_types = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truck_size = 10
    print(run(box_types, truck_size))
