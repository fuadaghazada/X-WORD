package aihw1;

/**
 *
 * @author cagatay.sel-ug
 */
import java.util.ArrayList;



public class State{
	
        //Problem constans
	public static final int LEFT_JUG_CAP = 7;	
	public static final int RIGHT_JUG_CAP = 5;
        
        public static final String CREATION_INITIAL = "Initial";
        public static final String CREATION_FILL_LEFT = "Filled left jug";
        public static final String CREATION_FILL_RIGHT = "Filled right jug";
        public static final String CREATION_EMPTY_LEFT = "Emptied left jug";
        public static final String CREATION_EMPTY_RIGHT = "Emptied right jug";
        public static final String CREATION_POUR_LEFT_TO_RIGHT = "Poured left to right";
        public static final String CREATION_POUR_RIGHT_TO_LEFT = "Poured right to left";          
        
        
        //Instance variables
	private int leftJugWater;
	private int rightJugWater;
        private String creation;
        private ArrayList<State> nextStates;        
        //To backtrack from goal state to initial state
        private State parent;
	
	public State(int leftJugWater,int rightJugWater,State parent,String creation){
	
		this.leftJugWater = leftJugWater;
		this.rightJugWater = rightJugWater;	
                this.parent = parent;
                this.creation = creation;
                this.nextStates = new ArrayList<State>();
                
		
	}
	
	public State fillLeftJug(){
		int leftJugWater = LEFT_JUG_CAP;
		int rightJugWater = this.rightJugWater;
		State newState = new State(leftJugWater,rightJugWater,this,CREATION_FILL_LEFT);
		return newState;
                
	}
	
	public State fillRightJug(){
		int rightJugWater = RIGHT_JUG_CAP;
		int leftJugWater = this.leftJugWater;
		State newState = new State(leftJugWater,rightJugWater,this, CREATION_FILL_RIGHT);
		return newState;
	}
	
	public State emptyLeftJug(){
		int leftJugWater=0;
		int rightJugWater = this.rightJugWater;
		State newState = new State(leftJugWater,rightJugWater,this, CREATION_EMPTY_LEFT );
		return newState;
	}
	public State emptyRightJug(){
		int rightJugWater=0;
		int leftJugWater = this.leftJugWater;
		State newState = new State(leftJugWater,rightJugWater,this,CREATION_EMPTY_RIGHT);
		return newState;
	}
	
	/**
	*Pour water from big to small jug
	*/
	public State pourLeftToRight(){
		
		int totalWater = this.leftJugWater + this.rightJugWater;
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
		State newState = new State(leftJugWater,rightJugWater,this,CREATION_POUR_LEFT_TO_RIGHT );
		return newState;
               
		
	}
	
	/**
	*Pour water from small to big jug
	*/
	public State pourRightToLeft(){
		
		int totalWater = this.leftJugWater + this.rightJugWater;
                int leftJugWater = -1;
		int rightJugWater = -1;
		
		//Pour all water from left to right and it does not exceed
		if(totalWater<=LEFT_JUG_CAP){
			leftJugWater = totalWater;
			rightJugWater = 0;
		}else if(totalWater>LEFT_JUG_CAP){
			leftJugWater = LEFT_JUG_CAP;
			rightJugWater = totalWater-leftJugWater;
		}
                State newState = new State(leftJugWater,rightJugWater,this,CREATION_POUR_RIGHT_TO_LEFT);
		return newState;
	}
        
        /**
         * This method back tracks states until initial state and reverses the order in order to print a path from root to leaf.
         */
        public void printPath(){
            State cur = this;
            ArrayList<State> path = new ArrayList<State>();
            while(cur!=null){
                path.add(cur);
                cur = cur.parent;
            }
            
            //Reverse printing the array
            for(int i=path.size()-1;i>=0;i--){
                cur = path.get(i);
                System.out.println("Step "+(path.size()-i ) +" : " + cur.creation);
                System.out.println(cur);                
            }
            
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
            /*str +="------Next States-----"+"\n";
            for(int i=0;i<nextStates.size();i++){
                State cur = nextStates.get(i);
                str += "Left jug water: "+cur.leftJugWater+
                        " Right jug water: " + cur.rightJugWater + "\n";
            }  */                 
            return str;
            
        }
        
        public ArrayList<State> getNextStates(){
            return nextStates;
        }
        
        public boolean isGoalState(int goal){
            
            if(leftJugWater == goal || rightJugWater == goal){
                return true;
            }else{
                return false;
            }
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