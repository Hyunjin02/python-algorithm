import java.util.HashMap;
import java.util.HashSet;

import javax.annotation.processing.Completion;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String,Integer> map = new HashMap();
    	String answer = "";
    	//참가자 세기
        for(String person : completion)
        	map.put(person, map.getOrDefault(person, 0) + 1);
        //완주자 계산
        for(String person1 : participant) {
        	if (map.containsKey(person1)) {
                map.put(person1, map.get(person1) - 1);
                if(map.get(person1)==0) {
                	map.remove(person1);
                }
        	}
        	else {
        		answer=person1;
        	}
        }
		return answer;
    }
}