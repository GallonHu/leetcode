package problem012

import "bytes"

func intToRoman1(num int) string {
	romanDigit := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	romanDesc := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}

	var buffer bytes.Buffer
	for num != 0 {
		for idx, r := range romanDigit {
			if num >= r {
				num -= r
				buffer.WriteString(romanDesc[idx])
				break
			}
		}
	}
	return buffer.String()
}

func intToRoman(num int) string {

	d := [4][]string{
		[]string{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"},
		[]string{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
		[]string{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
		[]string{"", "M", "MM", "MMM"},
	}
	return d[3][num/1000] +
		d[2][num/100%10] +
		d[1][num/10%10] +
		d[0][num%10]
}
