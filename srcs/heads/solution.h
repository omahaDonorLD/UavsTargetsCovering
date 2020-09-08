#ifndef UAVSCOVS_HEADS_SOLUTION_H_
#define UAVSCOVS_HEADS_SOLUTION_H_

#include <vector>
#include <igraph.h>
#include <glpk.h>
#include <map>

class Solution{

	vector<double*> uavs;// coordinates of uavs (vector of pointers to arrays)
	vector<int> *gcovs;// for each ground node, the indices of uavs covering it
	vector<vector<int>> uavcovs;// for each uav, the ground node it covers: inverse of gcovs

	// adjacency list of distances between uavs. Two structs:
	vector<vector<int>> outdeg;// 1. outdegree relations of uav. Note: uav j < uav outdeg[j] to avoid symmetries
	vector<vector<double>> distuav;// 2. dists[j][outdeg[j]] = distance between uav j and uav outdeg[j]
	//igraph_t* gr;// graph of the solution. Needed for connectivity checking

    void addTonetwork(double *toadd, double range);
    void connect_CCs(igraph_t* Gk, double range, vector<int>* uavsconnectivity, stack<tuple<int,int>>* pairs, bool dorestriction);
    void duplicate_uavs(double lb, int grndi, double range);
    void find_covers(int uavj, double range);// Find every covers of each ground node
    void populate(vector<int>* uavsconnectivity, double range, igraph_t* solnG0, stack<tuple<int,int>>* pairs);
    map<int,double>* solve_linear_model(double range, double lb);
    igraph_t* translate(double threshold, double* solverSln);
    bool uav_in_cover(vector<int> &gcovs, int uavindex);
    void updateDistMat(double range);

}



#endif // UAVSCOVS_HEADS_SOLUTION_H_
