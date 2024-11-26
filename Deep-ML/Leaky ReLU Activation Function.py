def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	return max(z,alpha*z)
