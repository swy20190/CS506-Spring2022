from collections import defaultdict
from math import inf
import random
import math
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    answer = [0]*len(points[0])
    for p in points:
        for i in range(len(p)):
            answer[i] += p[i]

    for i in range(len(answer)):
        answer[i] /= len(points)
    return answer


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    answer = []
    points_dict = {}
    for i in range(len(assignments)):
        if assignments[i] in points_dict:
            points_dict[assignments[i]].append(dataset[i])
        else:
            points_dict[assignments[i]] = [dataset[i]]

    for c in points_dict:
        center = [0]*len(points_dict[c][0])
        for point in points_dict[c]:
            for i in range(len(point)):
                center[i] += point[i]
        for i in range(len(center)):
            center[i] /= len(points_dict[c])

        answer.append(center)

    return answer


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return distance_squared(a, b)**(1/2)


def distance_squared(a, b):
    answer = 0
    for i in range(len(a)):
        answer += (a[i]-b[i])*(a[i]-b[i])
    return answer


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    res = []
    idc = random.sample(range(len(dataset)), k)
    for idx in idc:
        res.append(dataset[idx])
    return res


def cost_function(clustering):
    res = 0
    for center in clustering:
        d_sum = 0
        center_point = point_avg(clustering[center])
        for point in clustering[d_sum]:
            d_sum += distance(center_point, point)
        res += d_sum
    return res


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    res = []
    rest_idc = list(range(len(dataset)))
    selected_idc = []
    first = random.randint(0, len(dataset)-1)
    selected_idc.append(first)
    rest_idc.remove(first)
    for _ in range(k-1):
        weights = {}
        for rest_idx in rest_idc:
            w = 0
            for selected_idx in selected_idc:
                w += distance_squared(dataset[rest_idx], dataset[selected_idx])
            weights[rest_idx] = w
        w_sum = 0
        for idx in weights:
            w_sum += weights[idx]
        rand_s = random.randint(0, w_sum-2)
        acc = 0
        for idx in rest_idc:
            if acc<=rand_s and acc+weights[idx]>rand_s:
                selected_idc.append(idx)
                rest_idc.remove(idx)
                break
            else:
                acc += weights[idx]

    for idx in selected_idc:
        res.append(dataset[idx])

    return res


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
