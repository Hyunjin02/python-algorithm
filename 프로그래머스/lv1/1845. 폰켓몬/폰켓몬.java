import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashSet<Integer> hashSet = new HashSet<>();
        for (int num:nums) {
        	hashSet.add(num);
        }
        if(hashSet.size()>nums.length/2)
        	answer=nums.length/2;
        else
        	answer=hashSet.size();
        return answer;
    }
}