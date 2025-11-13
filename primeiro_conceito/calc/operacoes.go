package calc
import "fmt"
func Soma(nums... int) int {
	soma :=0
	for _, n := range nums {
		soma += n
	}
	return soma
}
func Multi(nums... int) int {
	if len(nums) == 0 {
		return 0
	}
	multi := 1
	for _, n := range nums {
		multi *= n
	}
	return multi
}
func Sub(nums... int) int {
	if len(nums) == 0 {
		return 0
	}
	sub := nums[0]
	for _, n := range nums[1:] {
		sub -= n
	}
	return sub
}
func Div(nums... int) int {
	if len(nums) == 0 {
		return 0
	}
	div := nums[0]
	for _, n := range nums[1:] {
		if n == 0 {
			fmt.Println("Erro: divisão por zero!")
			return 0
		}
		div /= n
	}
	return div
}