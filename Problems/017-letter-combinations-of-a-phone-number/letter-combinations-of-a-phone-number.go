package problem017

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}

	keyboards := map[byte]string{
		'2': "abc",
		'3': "def",
		'4': "ghi",
		'5': "jkl",
		'6': "mno",
		'7': "pqrs",
		'8': "tuv",
		'9': "wxyz",
	}

	res := []string{""}
	for _, d := range digits {
		temp := []string{}
		for _, x := range res {
			for _, y := range keyboards[byte(d)] {
				temp = append(temp, x+string(y))
			}
		}
		res = temp
	}
	return res
}
