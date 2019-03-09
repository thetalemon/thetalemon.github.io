<template>
  <div>
    <h2>↓画像↓</h2>
    <div v-if="uploadImage">
        <img :src="uploadImage">
    </div>
      <h2>↓結果↓</h2>
    <div v-if="processedImage">
        <img :src="processedImage">
    </div>
    <input type="file" @change="onFileChange">
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      uploadImage: '',
      processedImage: ''
    }
  },
  methods: {
    onFileChange (e) {
      e.preventDefault()
      var file = e.target.files[0]
      if (file && file.type.match(/^image\/(png|jpeg)$/)) {
        this.uploadImage = URL.createObjectURL(file)
      }
      this.postFile(URL.createObjectURL(file))
    },
    postFile (fileURL) {
      let formData = new FormData()
      formData.append('image', this.uploadImage)
      const path = `http://localhost:5000/cannyFile`
      axios.post(path, formData)
        .then(response => {
          this.processedImage = response.data.result
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
