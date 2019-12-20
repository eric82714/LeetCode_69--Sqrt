int mySqrt(int x){
    if(x == 0) return 0;
    else if(x == 1) return 1;
    else { 
        double result = x / 2;
        
        while(result * result > x + 0.1) {
            result = (result + x / result) / 2;
        }
        return (int)result;
    }
}
