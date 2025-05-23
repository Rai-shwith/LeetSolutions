<h2><a href="https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number">1482. How Many Numbers Are Smaller Than the Current Number</a></h2><h3>Easy</h3><hr><p>Given the array <code>nums</code>, for each <code>nums[i]</code> find out how many numbers in the array are smaller than it. That is, for each <code>nums[i]</code> you have to count the number of valid <code>j's</code> such that <code>j != i</code> <strong>and</strong> <code>nums[j] < nums[i]</code>.</p>

<p>Return the answer in an array.</p>

<p> </p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [8,1,2,2,3]
<strong>Output:</strong> [4,0,1,1,3]
<strong>Explanation:</strong> 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,5,4,8]
<strong>Output:</strong> [2,1,0,3]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,7,7,7]
<strong>Output:</strong> [0,0,0,0]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 <= nums.length <= 500</code></li>
	<li><code>0 <= nums[i] <= 100</code></li>
</ul>
