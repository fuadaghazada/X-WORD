/*
* CS461 - Artificial Intelligence HW1
* Group Members: Çağatay Sel, Utku Mert Topçuoğlu, Fuad Aghazada,Can Özgürel, Kaan Kıranbay
*
* Part a)
* Any water combination in big and small jug is a state. Instead of big and small, left and right jug terms were used in this program.
* Initial state is (0,0) state where both jugs are empty. Goal states for first question
are (x,1) or (1,x) where x is any amount of water. Goal states for second question are (3,x) and (x,3).
* There are 6 operators. These are fill left jug,fill right jug, empty left jug, empty right jug,pour left to right
and pour right to left.
* 6 operators create at most 6 new next state so branching factor is at most 6. However, some operations create same or visited states. Therefore, nodes 
have different branching factors.
*/

package aihw1;

import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

/**
 *
 * @author cagatay.sel-ug
 */
public class AIHW1 {

    public static int GOAL_LITER_1 = 1;
    public static int GOAL_LITER_3 = 3;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        System.out.println("-----------QUESTION 1-------------------");
        System.out.println("Goal: Reach "+GOAL_LITER_1 + " liter in a jug");
        System.out.println("Left jug water capacity: "+State.LEFT_JUG_CAP);
        System.out.println("Right jug water capacity: "+State.RIGHT_JUG_CAP);
        System.out.println();
        depthFirstSolve(GOAL_LITER_1);
        
        
        System.out.println("-----------QUESTION 2-------------------");
        System.out.println("Goal: Reach "+GOAL_LITER_3 + " liter in a jug");
        System.out.println("Left jug water capacity: "+State.LEFT_JUG_CAP);
        System.out.println("Right jug water capacity: "+State.RIGHT_JUG_CAP);
        System.out.println();
        breadthFirstSolve(GOAL_LITER_3);

    }

    ////////////Question 1 - Depth First Search for goal of 3 liter.///////////////////
    public static void depthFirstSolve(int goalLiter) {

        State initial = new State(0, 0, null, State.CREATION_INITIAL);
        //Keeping track of visited states to prevent looping
        ArrayList<State> visitedStates = new ArrayList<State>();
        State goal = depthFirstSearch(initial, goalLiter, visitedStates);

        if (goal == null) {
            System.out.println("Goal is unreachable");
        } else {
            System.out.println("Goal reached");
            goal.printPath();
            goal = null;

        }

    }

    ////////////Question 2 - Breadth First Search for goal of 1 liter.///////////////////

    public static void breadthFirstSolve(int goalLiter) {

        //Creating initial state
        State initial = new State(0, 0, null, State.CREATION_INITIAL);

        State goal = breadthFirstSearch(initial, goalLiter);

        if (goal == null) {
            System.out.println("Goal is unreachable");
        } else {
            System.out.println("Goal reached");
            goal.printPath();
            goal = null;

        }
    }

    /**
     * This method uses depth first search algorithm to find goal liter.
     * @param cur current state
     * @param goalLiter goal
     * @param visitedStates list of visited states
     * @return null or goal state
     */
    public static State depthFirstSearch(State cur, int goalLiter, ArrayList<State> visitedStates) {

        if (cur.isGoalState(goalLiter)) {
            return cur;
        }

        //Generating next states
        cur.generateNextStates(visitedStates);
        ArrayList<State> nextStates = cur.getNextStates();
        for (int i = 0; i < nextStates.size(); i++) {
            State goal = depthFirstSearch(nextStates.get(i), goalLiter, visitedStates);
            if (goal != null) {
                return goal;
            }
        }
        return null;

    }

    /**
     * This method uses breadth first search to solve jug problem.
     *
     * @param initial Initial state
     * @param goalLitre Goal liter that is searched
     * @return goal state or null
     */
    public static State breadthFirstSearch(State initial, int goalLiter) {

        Queue<State> queue = new LinkedList<>();
        //Keeping track of visited states to prevent looping
        ArrayList<State> visitedStates = new ArrayList<State>();
        visitedStates.add(initial);

        queue.add(initial);

        while (!queue.isEmpty()) {
            State cur = queue.remove();

            //Return if the current state is goal state
            if (cur.isGoalState(goalLiter)) {
                /* Printing visited nodes for debugging */
                /*System.out.println("---Visited State----");
                 System.out.println(cur);*/
                return cur;
            }

            //Generate next states
            cur.generateNextStates(visitedStates);
            ArrayList<State> nextStates = cur.getNextStates();

            //Add next states to queue
            for (int i = 0; i < nextStates.size(); i++) {
                queue.add(nextStates.get(i));
            }
        }
        return null;
    }

}