from statistics import median


def medians(nums1, nums2):
    return median(nums1 + nums2)


nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(medians(nums1, nums2))

