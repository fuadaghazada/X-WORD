/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aihw1;

import java.util.ArrayList;
/**
 *
 * @author cagatay.sel-ug
 */
public class AIHW1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        ArrayList<State> goalStates = new ArrayList<State>();
        goalStates.add(new State(0))
        
        
        State initial = new State(0,0);
        ArrayList<State> visitedStates = new ArrayList<State> ();
        visitedStates.add(initial);
       
        initial.generateNextStates(visitedStates);
        //System.out.println(visitedStates);
        System.out.println(initial);
    }
    
    public static void breadthFirstSearch(State initial){
        
        
        
    }
    
}
