package org.se.lab;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.List;

@RestController
public class ArticleController
{
    private final ArticleRepository repository;

    ArticleController(ArticleRepository repository)
    {
        this.repository = repository;
    }

    @GetMapping("v1/articles")
    List<Article> findAll()
    {
        return repository.findAll();
    }

    @GetMapping("v1/articles/{id}")
    Article findById(@PathVariable Long id)
    {
        return repository.findById(id).orElseThrow(() -> new ArticleNotFoundException(id));
    }

    @PostMapping("v1/articles")
    Article insert(@RequestBody Article newArticle)
    {
        return repository.save(newArticle);
    }

    @PutMapping("v1/articles/{id}")
    Article update(@RequestBody Article newArticle, @PathVariable Long id)
    {
        return repository.findById(id)
                .map(employee -> {
                    employee.setDescription(newArticle.getDescription());
                    employee.setPrice(newArticle.getPrice());
                    return repository.save(employee);
                })
                .orElseGet(() -> {
                    newArticle.setId(id);
                    return repository.save(newArticle);
                });
    }

    @DeleteMapping("v1/articles/{id}")
    void delete(@PathVariable Long id)
    {
        repository.deleteById(id);
    }
}
