package main // necessariario para importar o modulo utils, main = principal
//teste
import ( // imports de modulos necessários

	"GOLANG/utils" //usei o go mod init GOLANG para criar o modulo raiz
	"fmt"
	"math"
)

func main() { // função que roda ao iniciar o programa
	AreaDoCirculo()
}

func ConvertKmForMh() float32 {

fmt.Println("Vamos converter as distancias")
fmt.Println("Valor em KM:")

km := utils.ReadFloat32()[0]

mh := km / 1.60934
fmt.Printf("O valor de %.2f Km/h em M/h é: %.2f\n",km ,mh )
return mh
}

func ConvertMhForKM(){
	fmt.Println("Vamos converter as distancias")
	fmt.Println("Valor em M/h:")

	mh := utils.ReadFloat32()[0]

	km := mh * 1.60934
	fmt.Printf("O valor de %.2fM/h em Km/h é: %.2f",mh,km)
}

func Baskhara(a,b,c float64) {
delta := b*b - 4*a*c

	if delta < 0 {
		fmt.Print("Não existem raizes reais")
		return
	}

x1 := (-b + float64(math.Sqrt(float64(delta)))) / (2 * a)
x2 := (-b - float64(math.Sqrt(float64(delta)))) / (2* a)

fmt.Printf("as raizes da equação são x1 = %.2f e x2 = %.2f", x1,x2)

}

func AreaDoCirculo(){

	fmt.Println("Vamos calcular a ara do circulo, digite o valor do raio:")
	radio := utils.ReadFloat32()[0]
	area := math.Pi * float32(radio)


	fmt.Printf("A area do circulo de raio %.2f é: %.2f", radio, area)
}