import java.util.ArrayList;

public class State(){
	
	public static Final int LEFT_JUG_CAP = 7;	
	public static Final int RIGHT_JUG_CAP = 5;	


	private int leftJugWater;
	private int rightJugWater;
	
	public State(int leftJugWater,int rightJugWater){
	
		this.leftJugWater = leftJugWater;
		this.rightJugWater = rightJugWater;	
		
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
		
		totalWater = leftJugWater + rightJugWater;
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
		
		totalWater = leftJugWater + rightJugWater;
		
		//Pour all water from left to right and it does not exceed
		if(totalWater<LEFT_JUG_CAP){
			leftJugWater = totalWater;
			rightJugWater = 0;
		}else if(totalWater>LEFT_JUG_CAP_JUG_CAP){
			leftJugWater = LEFT_JUG_CAP;
			rightJugWater = totalWater-leftJugWater;
		}		
	}
	
	/**
	*This method generates possible states by applying the 6 operations defines above
	*/
	public ArrayList<State> generateNextStates(){
		
		ArrayList<State> nextStates = new ArrayList<State>();
		nextStates.add(fillLeftJug);
		nextStates.add(fillRightJug);
		nextStates.add(emptyLeftJug);
		nextStates.add(emptyRightJug);
		nextStates.add(pourLeftToRight);
		nextStates.add(pourRightToLeft);	
		return nextStates;
	}
	
	
}
