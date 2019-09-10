import spreadsheet_parser as sp
import json

'''
TODO
Caluclating volume, estimating 1RMs, calculating stress index,
e1RM progress graph, volume progress graph

'''

class DataAnalzer():

    def calculate_total_volume():
        pass

    def calculate_volume_per_category():
        pass

    def calculate_stress_index():
        pass

    def calculate_wilks():
        pass

    def caluclate_ipfpoints():
        pass

    def calculate_allometric():
        pass

    def calculate_modifier_effect():
        pass


class DataVisualizer():

    def __init__(self, mesocycles):
        self.mcs = mesocycles

    def print_mesocycles_cmd(self):
        workout_str_list = []
        for meso in self.mcs:
            print('*'*41*len(meso.microcycles[0].workouts))
            print('Mesocyle ' + meso.str())
            print('-'*41*len(meso.microcycles[0].workouts))
            for micro in meso.microcycles:
                print('Microcycle ' + micro.str())
                for workout in micro.workouts:
                    workout_str_list.append(workout.str())

                [print("D{:-<39d}".format(day, ' '), end='|') for day in range(1, len(workout_str_list)+1)]
                print('\n')
                for i in range(0,max([len(w) for w in workout_str_list])):
                    for j, w in enumerate(workout_str_list):
                        if i < len(w):
                            print("{:30s}-e1RM:{:4.1f} ".format(w[i][0][:30], w[i][1]) , end=" ")
                        else:
                            print(' '*41, end=" ")
                    print('\n')
                print('\n')
            print('*'*41*len(meso.microcycles[-1].workouts))

    def generate_e1RM_graph():
        pass

    def generate_volume_graph():
        pass

    def generate_bodyweight_graph():
        pass

    def generate_wilks_graph():
        pass

    def generate_competition_1RMs_graph():
        pass

