package apd1

import (
	"aprendendo_golang/utils" //usei o go mod init GOLANG para criar o modulo raiz/utils"
	"aprendendo_golang/primeiro_conceito/calc"
	"fmt"
)

func FazerAlgo() {
	nums := utils.ReadInt()
	result := calc.Multi(nums...)
	fmt.Println("a mult dos numeros é:", result)
}