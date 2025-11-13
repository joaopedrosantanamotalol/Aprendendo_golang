package teste_codigo

import (
	"GOLANG/utils"
	"GOLANG/calc"
	"fmt"
)

func FazerAlgo() {
	nums := utils.ReadInt()
	result := calc.Multi(nums...)
	fmt.Println("a mult dos numeros é:", result)
}