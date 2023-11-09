package cyou.kayacorp.productservice.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import cyou.kayacorp.productservice.model.Product;

public interface ProductRepository extends MongoRepository<Product, String>{

}
