package problem029

func divide(dividend int, divisor int) int {
	sign1, dividend := abs(dividend)
	sign2, divisor := abs(divisor)

	var cnt uint
	for divisor <= dividend {
		cnt++
		divisor <<= 1
	}

	res := 0
	for cnt > 0 {
		cnt--
		divisor >>= 1
		if divisor <= dividend {
			res += 1 << cnt
			dividend -= divisor
		}
	}

	if sign1 != sign2 {
		res = -res
	}

	if res < -(1<<31) || res > (1<<31)-1 {
		return 1<<31 - 1
	}
	return res
}

func abs(n int) (sign, num int) {
	sign = 1
	num = n
	if n < 0 {
		sign, num = -1, -n
	}
	return
}
