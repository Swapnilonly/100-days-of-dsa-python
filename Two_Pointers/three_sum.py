while left < right:
    total = nums[i] + nums[left] + nums[right]

    if total < 0:
        left += 1

    elif total > 0:
        right -= 1

    else:
        res.append([nums[i], nums[left], nums[right]])

        left += 1
        right -= 1

        while left < right and nums[left] == nums[left - 1]:
            left += 1

        while left < right and nums[right] == nums[right + 1]:
            right -= 1