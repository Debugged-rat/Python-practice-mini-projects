# Link for question: https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
import sys

def fit1(X, Y, x, y):
    crate_empty_space_x_axis = X % x
    crate_empty_space_y_axis = Y % y

    crate_filled_space_x_axis = X - crate_empty_space_x_axis
    crate_filled_space_y_axis = Y - crate_empty_space_y_axis

    max_number_of_boxes_on_x_axis = crate_filled_space_x_axis / x
    max_number_of_boxes_on_y_axis = crate_filled_space_y_axis / y

    max_number_of_boxes_in_crate = max_number_of_boxes_on_x_axis * max_number_of_boxes_on_y_axis

    return(max_number_of_boxes_in_crate)

print(int(fit1(12345, 678910, 1112, 1314)))
sys.exit()