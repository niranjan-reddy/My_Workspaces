package cyou.kayacorp.productservice.service;

import org.springframework.stereotype.Service;

import cyou.kayacorp.productservice.dto.ProductRequest;
import cyou.kayacorp.productservice.model.Product;
import cyou.kayacorp.productservice.repository.ProductRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Service
@RequiredArgsConstructor
@Slf4j
public class ProductService {
	
	private final ProductRepository productRepository;
	
/*	public ProductService(ProductRepository productRepository) {
		this.productRepository = productRepository;
	}*/
	
	public void createProduct(ProductRequest productRequest) {
		Product product = Product.builder()
				.name(productRequest.getName())
				.description(productRequest.getDescription())
				.price(productRequest.getPrice())
				.build();
		
		productRepository.save(product);
		log.info("Product {} is saved.", product.getId());
	}
}
