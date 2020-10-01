package internal

import "math"

// A place for common functionality that doesn't qualify as general utility.

func productInt(values ...int) int {
	result := 1
	for _, value := range values {
		result *= value
	}
	return result
}

func maxInt(values ...int) int {
	maxValue := math.MinInt16
	for _, value := range values {
		if value > maxValue {
			maxValue = value
		}
	}
	return maxValue
}

func minInt(values ...int) int {
	minValue := math.MaxInt16
	for _, value := range values {
		if value < minValue {
			minValue = value
		}
	}
	return minValue
}
