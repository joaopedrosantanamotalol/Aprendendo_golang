package utils //modulo utilitario para leitura de dados do usuario

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var reader = bufio.NewReader(os.Stdin)

// Leitura de uma linha de texto do usuario
func ReadText() string {
text, _ := reader.ReadString('\n')
return strings.TrimSpace(text)
}
// Leitura de um numero inteiro do usuario
func ReadInt() []int {
	for {
		text, _ := reader.ReadString('\n')//le e adciona um \n na string no final
		text = strings.TrimSpace(text)//remove espaços em branco no inicio e no fim da string
		strNums := strings.Fields(text)//divide a string em substrings separadas por espaços

		nums := make([]int, 0,len(strNums))//cria um slice de inteiros com o tamanho igual ao numero de substrings
		valid := true//flag para verificar se todos os numeros são validos

		for _, s := range strNums {//itera sobre as substrings
			n, err :=strconv.Atoi(s)//converte a substring para inteiro
			if err != nil{//se houver erro na conversão
				fmt.Println("Entrada invalida, tente novamente.")//mensagem de erro
				valid = false//atualiza a flag para falso
				break//sai do loop
			}
			nums = append(nums, n)//adiciona o numero convertido ao slice
	}
	if valid {//se todos os numeros forem validos
		return nums//retorna o slice de numeros
	}
}
}
// Leitura de um numero real simples do usuario
func ReadFloat32() []float32 {
	for {
		text, _ := reader.ReadString('\n')
		text = strings.TrimSpace(text)
		strNums := strings.Fields(text)

		nums := make([]float32, 0, len(strNums)) // <- slice vazio, com capacidade
		valid := true

		for _, s := range strNums {
			n, err := strconv.ParseFloat(s, 32)
			if err != nil {
				fmt.Println("Entrada inválida, tente novamente.")
				valid = false
				break
			}
			nums = append(nums, float32(n))
		}

		if valid {
			return nums
		}
	}
}

// Leitura de um numero real extenso do usuario
func ReadFloat64() []float64 {
	for {
		text, _ := reader.ReadString('\n')
		text = strings.TrimSpace(text)
		strNums := strings.Fields(text)

		nums := make([]float64, 0, len(strNums))
		valid := true

		for _, s := range strNums {
			n, err := strconv.ParseFloat(s, 64)
			if err != nil {
				fmt.Println("Entrada inválida, tente novamente.")
				valid = false
				break
			}
			nums = append(nums, n)
		}

		if valid {
			return nums
		}
	}
}
