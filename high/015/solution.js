// ===== 15. 三数之和 =====
// 难度: 中等
// 英文名: 3Sum
// 来源: https://leetcode.cn/problems/3sum/description/
//
// 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
// 
// 注意：答案中不可以包含重复的三元组。
// 
// 
// 
// 示例：
// 
// 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
// 
// 满足要求的三元组集合为：
// [
// [-1, 0, 1],
// [-1, -1, 2]
// ]
//
// ---------------------------------------------------------

function threeSum(nums) {
    const res=[],len=nums.length;
    nums.sort((a,b)=>a-b);

    for(let i=0;i<len;i++){
        let left=i+1,right=len-1,iNum=nums[i];
        if(i>0&&nums[i]===nums[i-1]){
            continue;
        }

        if(iNum>0){
            break;
        }

        while(left<right){
            let lNum=nums[left],rNum=nums[right],sum=iNum+rNum+lNum;

            if(sum<0){
                left++;
            }else if(sum>0){
                right--;
            }else{
                res.push([iNum,lNum,rNum]);
                while(left<right&&nums[left]===nums[left+1]){
                    left++;
                }
                while(left<right&&nums[right]===nums[right-1]){
                    right--;    
                }
                //!while这一块的逻辑要注意
                //!如果写成left++ right-- 会跳过一些重复的解
                // while(left<right&&nums[left]===nums[left-1]){
                //     left++;
                // }
                // while(left<right&&nums[right]===nums[right+1]){
                //     right--;    
                // }
                //!会漏掉一些情况
                left++;
                right--;
            }
        }
    }
    return res;
}

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
// console