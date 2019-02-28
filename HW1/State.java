/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aihw1;

/**
 *
 * @author cagatay.sel-ug
 */
import java.util.ArrayList;

public class State{
	
	public static final int LEFT_JUG_CAP = 7;	
	public static final int RIGHT_JUG_CAP = 5;	


	private int leftJugWater;
	private int rightJugWater;
        private ArrayList<State> nextStates;
	
	public State(int leftJugWater,int rightJugWater){
	
		this.leftJugWater = leftJugWater;
		this.rightJugWater = rightJugWater;	
                nextStates = new ArrayList<State>();
		
	}
	
	public State fillLeftJug(){
		int leftJugWater = LEFT_JUG_CAP;
		int rightJugWater = this.rightJugWater;
		State newState = new State(leftJugWater,rightJugWater);
		return newState;
	}
	
	public State fillRightJug(){
		int rightJugWater = RIGHT_JUG_CAP;
		int leftJugWater = this.leftJugWater;
		State newState = new State(leftJugWater,rightJugWater);
		return newState;
	}
	
	public State emptyLeftJug(){
		int leftJugWater=0;
		int rightJugWater = this.rightJugWater;
		State newState = new State(leftJugWater,rightJugWater);
		return newState;
	}
	public State emptyRightJug(){
		rightJugWater=0;
		int leftJugWater = this.leftJugWater;
		State newState = new State(leftJugWater,rightJugWater);
		return newState;
	}
	
	/**
	*Pour water from big to small jug
	*/
	public State pourLeftToRight(){
		
		int totalWater = leftJugWater + rightJugWater;
		int leftJugWater = -1;
		int rightJugWater = -1;
		
		//Pour all water from left to right and it does not exceed
		if(totalWater<=RIGHT_JUG_CAP){
			leftJugWater = 0;
			rightJugWater = totalWater;
		}else if(totalWater>RIGHT_JUG_CAP){
			rightJugWater = RIGHT_JUG_CAP;
			leftJugWater = totalWater-rightJugWater;
		}	
		State newState = new State(leftJugWater,rightJugWater);
		return newState;
               
		
	}
	
	/**
	*Pour water from small to big jug
	*/
	public State pourRightToLeft(){
		
		int totalWater = leftJugWater + rightJugWater;
		
		//Pour all water from left to right and it does not exceed
		if(totalWater<LEFT_JUG_CAP){
			leftJugWater = totalWater;
			rightJugWater = 0;
		}else if(totalWater>LEFT_JUG_CAP){
			leftJugWater = LEFT_JUG_CAP;
			rightJugWater = totalWater-leftJugWater;
		}
                State newState = new State(leftJugWater,rightJugWater);
		return newState;
	}
	
	/**
	*This method generates possible states by applying the 6 operations defines above
	*/
	public void generateNextStates(ArrayList<State> visitedStates){
		
		
		State newState = fillLeftJug();
                if(!visitedStates.contains(newState)){
                    this.nextStates.add(newState);
                    visitedStates.add(newState);
                }
                
		newState = fillRightJug();
                if(!visitedStates.contains(newState)){
                    this.nextStates.add(newState);
                    visitedStates.add(newState);
                }
                
		newState = emptyLeftJug();
                if(!visitedStates.contains(newState)){
                    this.nextStates.add(newState);
                    visitedStates.add(newState);
                }
                
		newState = emptyRightJug();
                if(!visitedStates.contains(newState)){
                    this.nextStates.add(newState);
                    visitedStates.add(newState);
                    
                }
                
		newState = pourLeftToRight();
                if(!visitedStates.contains(newState)){
                    this.nextStates.add(newState);
                    visitedStates.add(newState);
                }
                
		newState = pourRightToLeft();	
                if(!visitedStates.contains(newState)){
                    this.nextStates.add(newState);
                    visitedStates.add(newState);
                }		
	}
        
        @Override
        public String toString(){
            
            String str =  "Left jug water: "+ this.leftJugWater + " Right Jug Water: "+ this.rightJugWater+ "\n";
            str +="------Next States-----"+"\n";
            for(int i=0;i<nextStates.size();i++){
                State cur = nextStates.get(i);
                str += "Left jug water: "+cur.leftJugWater+
                        " Right jug water: " + cur.rightJugWater + "\n";
            }                   
            return str;
            
        }
        
        public ArrayList<State> getNextStates(){
            return nextStates;
        }
        
        
        
        @Override
        public boolean equals(Object o){
            
            State right = (State) o;
            
            if(right.leftJugWater == this.leftJugWater && right.rightJugWater == this.rightJugWater){
                return true;
            }
            return false;
        }
	
	
}