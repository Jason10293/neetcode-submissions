class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Guess the ship capacity to be sum of all element in the ship
        simulate how long it would take to ship all the elements
        if < days --> capacity can be decreased (decreased to what?)
        if > days --> capacity can be increased (increased to what?)
        min = largest element in the array
        
        min = 5
        max = 15
        mid = 10
        takes 2 days 

        min = 5
        max = 9
        mid = 7
        takes 3 days 

        min = 5
        max = 6
        mid = 5
        takes 3 days --> return 8
        """

        def simulate_packaging(weights, capacity): # How many days does it take to load all the packages for a given capacity
            ans = 1
            curr_capacity = 0
            for weight in weights:
                if curr_capacity + weight <= capacity:
                    curr_capacity += weight
                else:
                    curr_capacity = weight
                    ans += 1
            return ans
        
        min_weight = max(weights)
        max_weight = sum(weights)

        while min_weight < max_weight:
            mid = (min_weight + max_weight) // 2
            required_days = simulate_packaging(weights, mid)
            if required_days > days:
                min_weight = mid + 1
            else:
                max_weight = mid
        return min_weight
