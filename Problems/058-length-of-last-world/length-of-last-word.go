package problem058

import "strings"

func lengthOfLastWord(s string) int {
	s = strings.TrimSpace(s)
	if s == "" {
		return 0
	}

	sp := strings.Split(s, " ")
	return len(sp[len(sp)-1])
}
